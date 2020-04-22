
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;


void merge(int array[], int scratch[], int lo, int hi){
	int mid = lo + (hi-lo)/2; // either side of mid is sorted
	
	int L = lo;
	int H = mid+1;

	for ( int k=lo; k<=hi; ++k){
		if ( L<= mid and (H>hi or array[L] <= array[H]) ){ // H>hi means the second array is processed
			scratch[k] = array[L];
			L++;
		}
		else{
			scratch[k] = array[H];
			H++;
		}
	}


    // copying the sorted array from scratch
	for ( int k=lo; k<=hi; ++k){
		array[k] = scratch[k];
	}

	
	

}

void sort(int array[], int scratch[], int lo, int hi){

	
	if ( lo < hi){
		int mid = lo + (hi-lo)/2;
		sort(array,scratch,lo,mid);
		sort(array,scratch,mid+1,hi);
		merge(array,scratch,lo,hi);
	}

}


void megesort(int array[], const int length){
     
    int *scratch = new int[length-1];
	sort( array,scratch, 0, length-1);
	delete[] scratch ;


}


int main(int argc, char *argv[]){
       
  
	if (argc != 1) {
        cerr << "Usage: " << argv[0] << endl;
        return 1;
    }

    istringstream iss;
    cout << "Enter sequence of integers, each followed by a space: " << flush;
    int value, index = 0;
    vector<int> values;
    string str;
    str.reserve(11);
    char c;
    iss.clear();
    while (true) {
        c = getchar();
        const bool eoln = c == '\r' || c == '\n';
        if (isspace(c) || eoln) {
            if (str.length() > 0) {
                iss.str(str);
                if (iss >> value) {
                    values.push_back(value);
                } else {
                    cerr << "Error: Non-integer value '" << str
                         << "' received at index " << index << "." << endl;
                    return 1;
                }
                iss.clear();
                ++index;
            }
            if (eoln) {
                break;
            }
            str.clear();
        } else {
            str += c;
        }
    }

    int len  = values.size();
    if (len == 0) {
        cerr << "Error: Sequence of integers not received." << endl;
        return 1;
    }

    
	megesort( &values[0],len);
	cout << "Sorted array: " << endl;
	for ( int i=0; i<len; ++i){
		cout << values[i] << " ";
	}
	cout << endl; 

	return 0;


    


}


