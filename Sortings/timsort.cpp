#include <iostream>
#include <stdlib.h>
#include <vector>


using namespace std;



vector <int> InsertionSort(vector <int> arr, int length){
    for (int j = 1; j < length; j++){
            int value = arr[j];
            for (int i = j - 1; i >= 0 && value < arr[i]; i--) {
                arr[i + 1] = arr[i];
                arr[i] = value; 
           }
    }
    return arr;
}



 int MinRun(int length){
    int r = 0;
    while (length >= 64) {
        r |= length & 1;
        length >>= 1;
   }
    return length + r;
 }





 int* TimSort (int* array, int n){
    vector <int> run;
    vector<pair<int,int>>  run_arr;
    int min_r = MinRun(n), start = 0, r_size = 0;
    int i = 0;
    while (i <= n-1){
        if (array[i] < array[i+1]){
            run.push_back(array[i]);
            i++;
        }
        else{
            array[i] = array[i] ^ array[i+1];
            array[i+1] = array[i] ^ array[i+1];
            array[i] = array[i] ^ array[i+1];
            run.push_back(array[i]);
            run.push_back(array[i+1]);
            i+=2;
             if (run.size() < min_r){
                while (run.size() < min_r){
                    if (i < n){
                        run.push_back(array[i]);
                        i++;
                    }
                    else break;
                }
                run = InsertionSort(run, run.size());
                 for (int j = 0; j < run.size(); j++){
                      array[start+j] = run[j];
                 }
                 run_arr.push_back(make_pair(start, run.size()));
                 start = run.size()+start;
                run.clear();
            }
            else{
                 run = InsertionSort(run, run.size());
                 for (int j = 0; j < run.size(); j++){
                     array[start+j] = run[j];
                 }
                 run_arr.push_back(make_pair(start, run.size()));
                 start = run.size()+start;
                 run.clear();
            }

        }
    }
    i = 2;
    pair<int, int> x, y, z;
    if (run_arr.size() > 2){
        x = run_arr[0];
        y = run_arr[1]; 
        while (i  < run_arr.size()){
            z = run_arr[i];
            if (x.second <= y.second+z.second || y.second <= z.second){
                //merge y and min(x, z)
                vector <int> tmp;
                int k = 0, l = 0, n = 0, m = 0;
                if (x.second < z.second){
                    //merge x and y
                    int k = x.first, l = y.first, n = x.first + x.second, m = y.first + y.second;
                            while ((k < n) && (l < m)){
                                if (array[k] > array[l]){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                                if (array[k] < array[l]){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                                if (array[k] == array[l]){
                                    tmp.push_back(array[l]);
                                    tmp.push_back(array[k]);
                                    l++;
                                    k++;
                                }
                            }
                            if (k == n && l != m){
                                while(l < m){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                            }
                            if (l == m && k != n){
                                while(k < n){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                            }
                            k = l = 0;
                            for (int j = x.first; j < x.first + tmp.size(); j++){
                                array[j] = tmp[k];
                                k++;
                            }
                            x.second = x.first + tmp.size()+1;
                            tmp.clear();
                            if (i + 1 < run_arr.size()){
                                y = run_arr[i+1];
                                i+=1;
                                if (i + 1 < run_arr.size()){
                                    i++;
                                }
                                else{
                                    int k = x.first, l = y.first, n = x.first + x.second, m = y.first + y.second;
                                    while ((k < n) && (l < m)){
                                        if (array[k] > array[l]){
                                            tmp.push_back(array[l]);
                                            l++;
                                        }
                                        if (array[k] < array[l]){
                                            tmp.push_back(array[k]);
                                            k++;
                                        }
                                        if (array[k] == array[l]){
                                            tmp.push_back(array[l]);
                                            tmp.push_back(array[k]);
                                            l++;
                                            k++;
                                        }
                                    }
                                    if (k == n && l != m){
                                        while(l < m){
                                            tmp.push_back(array[l]);
                                            l++;
                                        }
                                    }
                                    if (l == m && k != n){
                                        while(k < n){
                                            tmp.push_back(array[k]);
                                            k++;
                                        }
                                    }
                                    k = l = 0;
                                    for (int j = x.first; j < x.first + tmp.size(); j++){
                                        array[j] = tmp[k];
                                        k++;
                                    }
                                    tmp.clear();
                                    i++;
                                }
                            }
                            else{
                                i++;
                            }
                }
                else{
                    //merge y and z
                    vector <int> tmp;
                    int k = y.first, l = z.first, n = y.first + y.second, m = z.first + z.second;
                    while ((k < n) && (l < m)){
                        if (array[k] > array[l]){
                            tmp.push_back(array[l]);
                            l++;
                        }
                        if (array[k] < array[l]){
                            tmp.push_back(array[k]);
                            k++;
                        }
                        if (array[k] == array[l]){
                            tmp.push_back(array[l]);
                            tmp.push_back(array[k]);
                            l++;
                            k++;
                        }
                    }
                    if (k == n){
                        while(l < m){
                            tmp.push_back(array[l]);
                            l++;
                        }
                    }
                    if (l == m){
                        while(k < n){
                            tmp.push_back(array[k]);
                            k++;
                        }
                    }
                    k = l = 0;
                    for (int j = y.first; j < y.first + tmp.size(); j++){
                        array[j] = tmp[k];
                        k++;
                    }
                    tmp.clear();
                    y.second = y.second + z.second;
                    if (i + 1 < run_arr.size()){
                        i++;
                    }
                    else{
                        int k = x.first, l = y.first, n = x.first + x.second, m = y.first + y.second;
                                    while ((k < n) && (l < m)){
                                        if (array[k] > array[l]){
                                            tmp.push_back(array[l]);
                                            l++;
                                        }
                                        if (array[k] < array[l]){
                                            tmp.push_back(array[k]);
                                            k++;
                                        }
                                        if (array[k] == array[l]){
                                            tmp.push_back(array[l]);
                                            tmp.push_back(array[k]);
                                            l++;
                                            k++;
                                        }
                                    }
                                    if (k == n && l != m){
                                        while(l < m){
                                            tmp.push_back(array[l]);
                                            l++;
                                        }
                                    }
                                    if (l == m && k != n){
                                        while(k < n){
                                            tmp.push_back(array[k]);
                                            k++;
                                        }
                                    }
                                    k = l = 0;
                                    for (int j = x.first; j < x.first + tmp.size(); j++){
                                        array[j] = tmp[k];
                                        k++;
                                    }
                                    tmp.clear();
                                    i++;
                    }
                }
                
                
            }
            else{
                // merge y and z
                vector <int> tmp;
                int k = y.first, l = z.first, n = y.first + y.second, m = z.first + z.second;
                while ((k < n) && (l < m)){
                    if (array[k] > array[l]){
                        tmp.push_back(array[l]);
                        l++;
                    }
                    if (array[k] < array[l]){
                        tmp.push_back(array[k]);
                        k++;
                    }
                    if (array[k] == array[l]){
                        tmp.push_back(array[l]);
                        tmp.push_back(array[k]);
                        l++;
                        k++;
                    }
                }
                if (k == n){
                    while(l < m){
                        tmp.push_back(array[l]);
                        l++;
                    }
                }
                if (l == m){
                    while(k < n){
                        tmp.push_back(array[k]);
                        k++;
                    }
                }
                k = l = 0;
                for (int j = y.first; j < y.first + tmp.size(); j++){
                    array[j] = tmp[k];
                    k++;
                }
                tmp.clear();
                y.second = y.second + z.second;
                if (i + 1 < run_arr.size()){
                    i++;
                }
                else{
                    //merge x and y
                     int k = x.first, l = y.first, n = x.first + x.second, m = y.first + y.second;
                            while ((k < n) && (l < m)){
                                if (array[k] > array[l]){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                                if (array[k] < array[l]){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                                if (array[k] == array[l]){
                                    tmp.push_back(array[l]);
                                    tmp.push_back(array[k]);
                                    l++;
                                    k++;
                                }
                            }
                            if (k == n && l != m){
                                while(l < m){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                            }
                            if (l == m && k != n){
                                while(k < n){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                            }
                            k = l = 0;
                            for (int j = x.first; j < x.first + tmp.size(); j++){
                                array[j] = tmp[k];
                                k++;
                            }
                            tmp.clear();
                            i++;
                }
            }
        }
    }
    if (run_arr.size() == 2){
        vector <int> tmp;
        x = run_arr[0];
        y = run_arr[1]; 
        int k = x.first, l = y.first, n = x.first + x.second, m = y.first + y.second;
                            while ((k < n) && (l < m)){
                                if (array[k] > array[l]){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                                if (array[k] < array[l]){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                                if (array[k] == array[l]){
                                    tmp.push_back(array[l]);
                                    tmp.push_back(array[k]);
                                    l++;
                                    k++;
                                }
                            }
                            if (k == n && l != m){
                                while(l < m){
                                    tmp.push_back(array[l]);
                                    l++;
                                }
                            }
                            if (l == m && k != n){
                                while(k < n){
                                    tmp.push_back(array[k]);
                                    k++;
                                }
                            }
                            k = l = 0;
                            for (int j = x.first; j < x.first + tmp.size(); j++){
                                array[j] = tmp[k];
                                k++;
                            }
                            tmp.clear();

    }

     for (int i = 0; i < n; i++){
         cout << array[i] << "  ";
     }
    return array;
 }


int main(){
    setlocale(LC_ALL,"Russian");
    int n, min_r;
    int* array;
    cout << "Введите размер сортируемого массива" << endl;
    cin >> n;
    for (int i = 0; i < n; i++){
        array[i] = rand() % 100;
        cout << array[i] << "  ";
    }
    cout << endl;
    array = TimSort(array, n);
}