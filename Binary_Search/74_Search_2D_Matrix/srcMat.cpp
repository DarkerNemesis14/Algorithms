class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int mid;
        int l = 0;
        int r = matrix[0].size() - 1;
        int u = 0;
        int d = matrix.size() - 1;

        while(u<d) {
            mid = u + (d - u) / 2;
            if(matrix[mid][0] == target) {
                return true;
            }
            else if(matrix[mid][0] < target) {
                if(matrix[mid + 1][0] > target) {
                    u = mid;
                    break;
                }
                else {
                    u = mid + 1;
                }
            }
            else {
                d = mid - 1;
            }
        }

        while(l<=r) {
            mid = l + (r - l) / 2;
            if(matrix[u][mid] == target) {
                return true;
            }
            else if(matrix[u][mid] < target) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        return false;
    }
};