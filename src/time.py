class Timer:

    def __init__(self, time, duration, clock):
        self.clock = clock

        self.start_time = time
        self._duration = duration

    def _remove_from_clock(self):
        self.clock.remove(self)

    @property
    def complete(self):
        finished = bool(self.elapsed >= self._duration)
        return finished

    @property
    def percent(self):
        return self.elapsed / self._duration

    @property
    def elapsed(self):
        elapsed = self.clock.time_since(self.start_time)
        if elapsed >= self.duration:
            self._remove_from_clock()
        return elapsed

    @property
    def duration(self):
        return self._duration


class Loop(Timer):

    def __init__(self, time, loop_length, clock):
        super().__init__(time, loop_length, clock)

    @property
    def elapsed(self):
        return self.clock.time_since(self.start_time) % self.duration


class Clock:

    def __init__(self, step=1):
        self._elapsed = 0
        self._delta = 0
        self.time_step = step
        self.timers: list[Timer] = []
        self.running = True

    def time_since(self, start_time):
        return self._elapsed - start_time if start_time >= 0.0 else 0

    def remove_timer(self, item: Timer):
        self.timers.remove(item)

    def new_timer(self, length):
        timer = Timer(self._elapsed, length, self)
        self.timers.append(timer)
        return timer

    def new_loop(self, length):
        timer = Loop(self._elapsed, length, self)
        self.timers.append(timer)
        return timer

    def tick(self, delta_time):
        self._delta = delta_time*self.time_step*self.running
        self._elapsed += self.delta_time

    def pause(self):
        self.running = False

    def run(self):
        self.running = True

    @property
    def delta_time(self):
        return self._delta

    @property
    def elapsed(self):
        return self._elapsed

    @property
    def time(self):
        return self._elapsed


class GlobalClock(Clock):

    def __init__(self):
        super().__init__()
        self.frame_count = 0
        self.clocks: list[Clock] = [Clock(1)]

    def tick(self, delta_time):
        self.frame_count += 1
        self._delta = delta_time*self.time_step*self.running
        self._delta += self.delta_time
        for clock in self.clocks:
            clock.tick(delta_time)

    def remove_clock(self, clock):
        self.clocks.remove(clock)

    def add_clock(self, clock):
        self.clocks.append(clock)

    def frames_since(self, start_frame):
        return self.frame_count - start_frame


GLOBAL_CLOCK: GlobalClock = GlobalClock()
LOCAL_CLOCK: Clock = GLOBAL_CLOCK.clocks[0]
