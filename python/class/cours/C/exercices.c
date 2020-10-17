#include <stdio.h>

// recuperer la saisis de 5 notes de l utisateur et en resortir la moyenne 


int saisir (int* nombre_de_notes){

    // int i;
    // i = 0;
    

    float notes [*nombre_de_notes]; 


    for (int i = 0; i > *nombre_de_notes; i++){

    
        printf("saisir note numero %d : ", *nombre_de_notes);
        scanf("%f", &notes[i]);

    }
    return notes;
    

}

float CalculMoyenne(float notes [], int nombre_de_notes){
    float* ma_moyenne;
    *ma_moyenne = 0.0;

    for(int i = 0; i < nombre_de_notes; i++)
    {
        *ma_moyenne += notes[i];
    }
    printf("La moyenne de %d notes rentrees est : %f", nombre_de_notes, ma_moyenne);


}


int main(){

    int *nombre_de_notes;
    
    printf("combien de note voulez vous rentrez ?");
    scanf("%d", &nombre_de_notes);

    CalculMoyenne(saisir(nombre_de_notes), *nombre_de_notes);
    return 0;

}