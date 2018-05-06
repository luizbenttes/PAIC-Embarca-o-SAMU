#include <stdio.h>


double bezier(double A,  // Start value
              double B,  // First control value
              double C,  // Second control value
              double D,  // Ending value
              double t)  // Parameter 0 <= t <= 1
{
    double s = 1 - t;
    double AB = A*s + B*t;
    double BC = B*s + C*t;
    double CD = C*s + D*t;
    double ABC = AB*s + CD*t;
    double BCD = BC*s + CD*t;
    return ABC*s + BCD*t;
}

main()
{
        double a,b,c,d,t;
        int vector[100];
        a = 0.0f;
        b = 19.70f;
        c = 106.19f;
        d = 124.0f;
        t = 0.0f;
        int i = 0;
        printf("Start. A=%f, B=%f, C=%f, D=%f, t=%f\n", a,b,c,d,t);

        while(1)
        {   
                if(t>1.0f)
                        break;
                i = i+1;
                vector[i]= bezier(a,b,c,d,t);
                printf("Bezier pt= %f\n", );

                t += 0.01f;
        } 
        for(int i=0; i < 100;i++){
            printf("%f,",vector[i]);
        }
        return 1;
}