class Solution {
public:
    bool isMonotonic(vector<int>& arr) {
        bool inc=true;
        bool dec=true;
        int n= arr.size()-1;
        for(int i=0;i<n;i++){
            if(arr[i]<arr[i+1]){
                dec=false;
            }
            if(arr[i]>arr[i+1]){
                inc=false;
            }
            
        }
      return inc||dec;  
    }
};