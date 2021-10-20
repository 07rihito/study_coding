#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const* argv[])
{
  int N;
  cin >> N;
  int A[N];
  for (int i = 0; i < N; i++) {
    cin >> A[i];

  }

  int count = 0;

  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
      if ((A[i]-A[j]) % 200 == 0) {
        count ++;
      }
    }
  }

  cout << count << endl;
  return 0;
}