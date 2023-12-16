class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        vector<int> ret;

        while(i<j) {
            int sum = numbers[i] + numbers[j];
            if(sum == target){
                ret.push_back(i + 1);
                ret.push_back(j + 1);
                break;
            }
            else if(sum < target){
                i++;
            }
            else {
                j--;
            }

        }
        return ret;
    }
};