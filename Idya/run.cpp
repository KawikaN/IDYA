#include <iostream>
#include <windows.h>

using namespace std;


int main(){

    

    POINT p;
    HDC hdc = GetDC(NULL);
    COLORREF color = GetPixel(hdc, 0, 0);
    ReleaseDC(NULL, hdc);

    cout << color;

    return 0;
}