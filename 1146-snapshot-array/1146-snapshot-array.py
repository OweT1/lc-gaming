class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0]*length
        self.snapshots = []
        self.curr_snapshot = {i: 0 for i in range(length)}
        self.curr_snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.curr_snapshot[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.curr_snapshot.copy())
        self.curr_snapshot = {}
        self.curr_snap_id += 1
        return self.curr_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id == self.curr_snap_id:
            return self.arr[index]
        
        snapshot_history = self.snapshots[:snap_id+1]
        for history in reversed(snapshot_history):
            if index in history:
                return history[index]