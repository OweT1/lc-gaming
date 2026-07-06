class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const vector<int> a, const vector<int> b){
            return a[1] <= b[1];
        });
        std::sort(intervals.begin(), intervals.end(), [](const vector<int> a, const vector<int> b){
            return a[0] <= b[0];
        });

        int res = 0;
        for (int i=0; i<intervals.size(); i++) {
            vector<int> curr = intervals[i];
            // for (int k: curr) std::cout << k << " ";
            for (int j=0; j<i; j++) {
                vector<int> cmp = intervals[j];
                if (curr[0] >= cmp[0] && curr[1] <= cmp[1]) {
                    res--;
                    break;
                }
            }
            res++;
            // std::cout << "\n";
        }

        return res;
    }
};