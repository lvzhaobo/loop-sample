"""
番茄时钟核心逻辑单元测试
"""
import sys
import os
import unittest

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pomodoro_core import (
    format_time,
    get_phase_duration,
    get_phase_label,
    switch_phase,
    tick,
    WORK_SECONDS,
    BREAK_SECONDS
)


class TestPomodoroCore(unittest.TestCase):
    """测试番茄时钟核心逻辑"""

    def test_format_time_zero(self):
        """测试0秒格式化为00:00"""
        self.assertEqual(format_time(0), "00:00")

    def test_format_time_normal(self):
        """测试正常时间格式化"""
        self.assertEqual(format_time(1500), "25:00")  # 25分钟
        self.assertEqual(format_time(300), "05:00")   # 5分钟
        self.assertEqual(format_time(61), "01:01")
        self.assertEqual(format_time(3661), "61:01")

    def test_format_time_negative(self):
        """测试负数秒数应返回00:00"""
        self.assertEqual(format_time(-1), "00:00")
        self.assertEqual(format_time(-100), "00:00")

    def test_get_phase_duration_work(self):
        """测试工作阶段时长"""
        self.assertEqual(get_phase_duration('work'), WORK_SECONDS)
        self.assertEqual(get_phase_duration('work'), 1500)

    def test_get_phase_duration_break(self):
        """测试休息阶段时长"""
        self.assertEqual(get_phase_duration('break'), BREAK_SECONDS)
        self.assertEqual(get_phase_duration('break'), 300)

    def test_get_phase_duration_invalid(self):
        """测试无效阶段应抛出异常"""
        with self.assertRaises(ValueError):
            get_phase_duration('invalid')

    def test_get_phase_label_work(self):
        """测试工作阶段标签"""
        self.assertEqual(get_phase_label('work'), '工作时段')

    def test_get_phase_label_break(self):
        """测试休息阶段标签"""
        self.assertEqual(get_phase_label('break'), '休息时段')

    def test_get_phase_label_invalid(self):
        """测试无效阶段应抛出异常"""
        with self.assertRaises(ValueError):
            get_phase_label('invalid')

    def test_switch_phase_work_to_break(self):
        """测试工作切换到休息"""
        self.assertEqual(switch_phase('work'), 'break')

    def test_switch_phase_break_to_work(self):
        """测试休息切换到工作"""
        self.assertEqual(switch_phase('break'), 'work')

    def test_switch_phase_invalid(self):
        """测试无效阶段应抛出异常"""
        with self.assertRaises(ValueError):
            switch_phase('invalid')

    def test_tick_normal(self):
        """测试正常滴答（剩余时间>0）"""
        result = tick(100, 'work')
        self.assertEqual(result['remaining'], 99)
        self.assertEqual(result['phase'], 'work')
        self.assertFalse(result['switched'])

    def test_tick_zero(self):
        """测试剩余时间为0时切换阶段"""
        result = tick(0, 'work')
        self.assertEqual(result['phase'], 'break')
        self.assertEqual(result['remaining'], BREAK_SECONDS)
        self.assertTrue(result['switched'])

    def test_tick_negative(self):
        """测试剩余时间为负数时切换阶段"""
        result = tick(-1, 'work')
        self.assertEqual(result['phase'], 'break')
        self.assertEqual(result['remaining'], BREAK_SECONDS)
        self.assertTrue(result['switched'])

    def test_tick_break_to_work(self):
        """测试休息阶段结束切换到工作"""
        result = tick(0, 'break')
        self.assertEqual(result['phase'], 'work')
        self.assertEqual(result['remaining'], WORK_SECONDS)
        self.assertTrue(result['switched'])

    def test_work_seconds_constant(self):
        """测试工作秒数常量"""
        self.assertEqual(WORK_SECONDS, 1500)

    def test_break_seconds_constant(self):
        """测试休息秒数常量"""
        self.assertEqual(BREAK_SECONDS, 300)


if __name__ == '__main__':
    unittest.main()