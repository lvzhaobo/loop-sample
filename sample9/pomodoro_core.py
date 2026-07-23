"""
番茄时钟核心逻辑模块
纯函数实现，无副作用，便于单元测试
"""

# 默认时长（秒）
DEFAULT_WORK_TIME = 25 * 60  # 25分钟
DEFAULT_BREAK_TIME = 5 * 60  # 5分钟


def create_state(work_time=None, break_time=None):
    """
    创建初始计时状态
    
    Args:
        work_time: 工作时长（秒），默认25分钟
        break_time: 休息时长（秒），默认5分钟
    
    Returns:
        dict: 包含计时状态信息的字典
    """
    return {
        'remaining_seconds': work_time or DEFAULT_WORK_TIME,
        'current_phase': 'work',  # 'work' 或 'break'
        'loop_count': 0,
        'is_running': False,
        'work_time': work_time or DEFAULT_WORK_TIME,
        'break_time': break_time or DEFAULT_BREAK_TIME
    }


def tick(state):
    """
    计时器滴答一次（减少1秒）
    
    Args:
        state: 当前状态字典
    
    Returns:
        dict: 更新后的状态字典（新对象）
    """
    new_state = dict(state)
    
    if new_state['remaining_seconds'] <= 0:
        # 时段结束，切换
        return switch_phase(new_state)
    
    new_state['remaining_seconds'] -= 1
    return new_state


def switch_phase(state):
    """
    切换工作/休息时段
    
    Args:
        state: 当前状态字典
    
    Returns:
        dict: 切换后的状态字典
    """
    new_state = dict(state)
    
    if new_state['current_phase'] == 'work':
        # 工作结束，进入休息
        new_state['current_phase'] = 'break'
        new_state['remaining_seconds'] = new_state['break_time']
        new_state['loop_count'] += 1
    else:
        # 休息结束，进入工作
        new_state['current_phase'] = 'work'
        new_state['remaining_seconds'] = new_state['work_time']
    
    return new_state


def reset_state(state):
    """
    重置状态到初始工作时段
    
    Args:
        state: 当前状态字典
    
    Returns:
        dict: 重置后的状态字典
    """
    return {
        'remaining_seconds': state['work_time'],
        'current_phase': 'work',
        'loop_count': 0,
        'is_running': False,
        'work_time': state['work_time'],
        'break_time': state['break_time']
    }


def format_time(total_seconds):
    """
    将秒数格式化为 MM:SS 格式
    
    Args:
        total_seconds: 总秒数（非负整数）
    
    Returns:
        str: 格式化后的时间字符串，如 "25:00"
    """
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def get_phase_label(phase):
    """
    获取时段的中文标签
    
    Args:
        phase: 'work' 或 'break'
    
    Returns:
        str: 中文标签
    """
    if phase == 'work':
        return '工作时段'
    elif phase == 'break':
        return '休息时段'
    return '未知'