from src.loop_timer import LoopTimer

if __name__ == '__main__':
	
	LoopTimer.run(lambda x: 2**x, 100, batch_size = 10)