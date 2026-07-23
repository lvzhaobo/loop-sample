"""
番茄时钟核心逻辑单元测试
"""
import sys
import os
import unittest

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pomodoro_core import (
    create_state,
    tick,
    switch_phase,
    reset_state,
    format_time,
    get_phase_label,
    DEFAULT_WORK_TIME,
    DEFAULT_BREAK_TIME
)


class TestPomodoroCore(unittest.TestCase):
    """测试番茄时钟核心逻辑"""

    def test_create_state_default(self):
        """测试默认状态创建"""
        state = create_state()
        self.assertEqual(state['remaining_seconds'], DEFAULT_WORK_TIME)
        self.assertEqual(state['current_phase'], 'work')
        self.assertEqual(state['loop_count'], 0)
        self.assertFalse(state['is_running'])
        self.assertEqual(state['work_time'], DEFAULT_WORK_TIME)
        self.assertEqual(state['break_time'], DEFAULT_BREAK_TIME)

    def test_create_state_custom(self):
        """测试自定义时长状态创建"""
        state = create_state(work_time=1500, break_time=300)
        self.assertEqual(state['remaining_seconds'], 1500)
        self.assertEqual(state['work_time'], 1500)
        self.assertEqual(state['break_time'], 300)

    def test_tick_decrease(self):
        """测试tick减少剩余时间"""
        state = create_state(work_time=10, break_time=5)
        state['remaining_seconds'] = 10
        new_state = tick(state)
        self.assertEqual(new_state['remaining_seconds'], 9)
        self.assertEqual(new_state['current_phase'], 'work')

    def test_tick_switch_to_break(self):
        """测试tick在剩余时间为0时切换到休息"""
        state = create_state(work_time=10, break_time=5)
        state['remaining_seconds'] = 0
        new_state = tick(state)
        self.assertEqual(new_state['current_phase'], 'break')
        self.assertEqual(new_state['remaining_seconds'], 5)
        self.assertEqual(new_state['loop_count'], 1)

    def test_tick_switch_to_work(self):
        """测试tick在休息结束时切换到工作"""
        state = create_state(work_time=10, break_time=5)
        state['current_phase'] = 'break'
        state['remaining_seconds'] = 0
        new_state = tick(state)
        self.assertEqual(new_state['current_phase'], 'work')
        self.assertEqual(new_state['remaining_seconds'], 10)
        self.assertEqual(new_state['loop_count'], 0)

    def test_switch_phase_work_to_break(self):
        """测试从工作切换到休息"""
        state = create_state(work_time=10, break_time=5)
        new_state = switch_phase(state)
        self.assertEqual(new_state['current_phase'], 'break')
        self.assertEqual(new_state['remaining_seconds'], 5)
        self.assertEqual(new_state['loop_count'], 1)

    def test_switch_phase_break_to_work(self):
        """测试从休息切换到工作"""
        state = create_state(work_time=10, break_time=5)
        state['current_phase'] = 'break'
        new_state = switch_phase(state)
        self.assertEqual(new_state['current_phase'], 'work')
        self.assertEqual(new_state['remaining_seconds'], 10)
        self.assertEqual(new_state['loop_count'], 0)

    def test_reset_state(self):
        """测试重置状态"""
        state = create_state(work_time=10, break_time=5)
        state['remaining_seconds'] = 3
        state['current_phase'] = 'break'
        state['loop_count'] = 5
        new_state = reset_state(state)
        self.assertEqual(new_state['remaining_seconds'], 10)
        self.assertEqual(new_state['current_phase'], 'work')
        self.assertEqual(new_state['loop_count'], 0)
        self.assertFalse(new_state['is_running'])

    def test_format_time_normal(self):
        """测试时间格式化"""
        self.assertEqual(format_time(1500), '25:00')
        self.assertEqual(format_time(0), '00:00')
        self.assertEqual(format_time(61), '01:01')
        self.assertEqual(format_time(3600), '60:00')

    def test_format_time_negative(self):
        """测试负数时间格式化"""
        self.assertEqual(format_time(-1), '00:00')

    def test_get_phase_label_work(self):
        """测试工作时段标签"""
        self.assertEqual(get_phase_label('work'), '工作时段')

    def test_get_phase_label_break(self):
        """测试休息时段标签"""
        self.assertEqual(get_phase_label('break'), '休息时段')

    def test_get_phase_label_unknown(self):
        """测试未知时段标签"""
        self.assertEqual(get_phase_label('unknown'), '未知')


if __name__ == '__main__':
    unittest.main()