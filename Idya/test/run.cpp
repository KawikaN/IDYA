#include <iostream>
#include <windows.h>

using namespace std;


int main(){

    HDC dc = GetDC(NULL);
    COLORREF color = GetPixel(dc, 1851, 68);
    ReleaseDC(NULL, dc);


    cout << color;

    return 0;
}