#include <iostream>
using namespace std;

// despliega contenido del array por pantalla
void muestra(int a[], int l) {
    cout << "[ ";
    for (int i = 0; i < l; i++) {
        cout << a[i] << " ";
    }
    cout << "]\n";
}

// retorna posición mínima no asignada aún
int posicionMinimo(int a[], int asignado[], int l) {
    int posmin = -99;
    int valmin = 99999;
    for (int i = 0; i < l; i++) {
        if (!asignado[i] && a[i] < valmin) {
            posmin = i;
            valmin = a[i];
        }
    }
    asignado[posmin] = 1;
    return posmin;
}

void ImhotepSort(int a[], int l) {
}

int main(int argc, char* argv[]) {
    int a[] = {7, 3, 4, 1, 2, 8, 3, 4, 3};
    cout << "---original--- ";
    muestra(a, 9);
    ImhotepSort(a, 9);
    cout << "---ordenado--- ";
    muestra(a, 9); // [ 1 3 3 4 8 7 4 3 2 ]
    cout << endl;

    int b[] = {15, 83, 92, 36, 12, 49, 52, 36, 64, 81, 11, 23, 47, 36};
    cout << "---original--- ";
    muestra(b, 14);
    ImhotepSort(b, 14);
    cout << "---ordenado--- ";
    muestra(b, 14); // [ 11 15 36 36 49 64 83 92 81 52 47 23 12 ]
    return 0;
}
