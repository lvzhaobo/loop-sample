"""
番茄时钟核心逻辑模块
纯函数实现，无副作用，便于单元测试
"""

# 默认时间配置（秒）
WORK_SECONDS = 25 * 60  # 25分钟
BREAK_SECONDS = 5 * 60  # 5分钟


def format_time(total_seconds: int) -> str:
    """
    将秒数格式化为 MM:SS 格式

    Args:
        total_seconds: 总秒数（非负整数）

    Returns:
        格式化的时间字符串，如 "25:00"
    """
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def get_phase_duration(phase: str) -> int:
    """
    获取指定阶段的时长（秒）

    Args:
        phase: 阶段名称，'work' 或 'break'

    Returns:
        对应阶段的时长（秒）
    """
    if phase == 'work':
        return WORK_SECONDS
    elif phase == 'break':
        return BREAK_SECONDS
    else:
        raise ValueError(f"未知阶段: {phase}")


def get_phase_label(phase: str) -> str:
    """
    获取阶段的中文标签

    Args:
        phase: 阶段名称，'work' 或 'break'

    Returns:
        中文标签字符串
    """
    if phase == 'work':
        return '工作时段'
    elif phase == 'break':
        return '休息时段'
    else:
        raise ValueError(f"未知阶段: {phase}")


def switch_phase(current_phase: str) -> str:
    """
    切换阶段（工作→休息 或 休息→工作）

    Args:
        current_phase: 当前阶段

    Returns:
        切换后的阶段
    """
    if current_phase == 'work':
        return 'break'
    elif current_phase == 'break':
        return 'work'
    else:
        raise ValueError(f"未知阶段: {current_phase}")


def tick(remaining: int, phase: str) -> dict:
    """
    计时器滴答一次，返回新的状态

    Args:
        remaining: 剩余秒数
        phase: 当前阶段

    Returns:
        包含新剩余秒数和新阶段的字典
        {'remaining': int, 'phase': str, 'switched': bool}
    """
    if remaining <= 0:
        new_phase = switch_phase(phase)
        new_remaining = get_phase_duration(new_phase)
        return {'remaining': new_remaining, 'phase': new_phase, 'switched': True}
    else:
        return {'remaining': remaining - 1, 'phase': phase, 'switched': False}