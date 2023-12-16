class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int j = 0;
        int maxPro = 0;

        while(j<prices.size()) {
            if(prices[i] > prices[j]) {
                i = j;
            }
            else {
                maxPro = max(maxPro, prices[j] - prices[i]);
            }
            j++;
        }
        return maxPro;
    }
};