# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用函式封裝計算、以 if 判斷輸入，並用串列推導式產生軌跡座標。
# 計算拋體運動的軌跡與可命中的發射角度。
# 依輸入距離繪製射程概覽及可達範圍圖。
import math

import matplotlib.pyplot as plt


SPEED = 500 / 3.6  # km/h to m/s
GRAVITY = 9.81
MAX_RANGE = SPEED ** 2 / GRAVITY


def launch_angles(distance):
	if distance < 0:
		raise ValueError("目標距離不可為負數")
	if distance > MAX_RANGE:
		return ()

	low_angle = math.degrees(math.asin(min(1.0, distance / MAX_RANGE))) / 2
	return (low_angle, 90 - low_angle)


def trajectory(angle, samples=101):
	radians = math.radians(angle)
	flight_time = 2 * SPEED * math.sin(radians) / GRAVITY
	times = [flight_time * step / (samples - 1) for step in range(samples)]
	horizontal = [SPEED * math.cos(radians) * time for time in times]
	vertical = [SPEED * math.sin(radians) * time - GRAVITY * time ** 2 / 2 for time in times]
	return horizontal, vertical


def plot_trajectories(distance):
	angles = launch_angles(distance)
	figure, (overview, closeup) = plt.subplots(2, 1, figsize=(10, 8))

	for angle in range(1, 90):
		horizontal, vertical = trajectory(angle)
		for axes in (overview, closeup):
			axes.plot(horizontal, vertical, color="steelblue", alpha=0.12)

	for name, angle in zip(("Low angle", "High angle"), angles):
		horizontal, vertical = trajectory(angle)
		for axes in (overview, closeup):
			axes.plot(horizontal, vertical, linewidth=2, label=f"{name}: {angle:.2f}°")

	for axes in (overview, closeup):
		axes.axhline(0, color="black", linewidth=0.8)
		axes.set_ylabel("Height (m)")
		axes.grid(True)
		if angles:
			axes.scatter(distance, 0, color="red", zorder=3)
			axes.legend()

	overview.set_xlim(0, 1000)
	overview.set_xticks(range(0, 1001, 100))
	overview.set_title("1 km range (100 m intervals)")
	closeup.set_xlim(0, MAX_RANGE * 1.05)
	closeup.set_title("Reachable range (close-up)")
	closeup.set_xlabel("Horizontal distance (m)")
	figure.tight_layout()
	plt.show()


if __name__ == "__main__":
	try:
		target = float(input("請輸入目標距離 (m)："))
		solutions = launch_angles(target)
		if solutions:
			print(f"發射角度：{solutions[0]:.2f}° 或 {solutions[1]:.2f}°")
		else:
			print(f"無法命中：100 km/h 的最大射程約 {MAX_RANGE:.2f} m")
		plot_trajectories(target)
	except ValueError as error:
		print(f"輸入錯誤：{error}")
