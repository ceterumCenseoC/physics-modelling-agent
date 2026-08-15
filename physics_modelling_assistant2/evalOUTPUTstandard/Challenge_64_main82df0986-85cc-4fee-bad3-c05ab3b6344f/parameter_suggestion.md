.md
```json
{
  "model_name": "2D Ising CFT 5-Point Function",
  "description": "Calculates the correlation function <epsilon(x1)epsilon(x2)epsilon(x3)sigma(x4)sigma(x5)>.",
  "parameters": [
    {
      "name": "central_charge",
      "value": 0.5,
      "unit": "dimensionless",
      "derivation": "The central charge c for the minimal model M(4,3) (Ising model) is c = 1/2.",
      "source": "P. Di Francesco, P. Mathieu, and D. Sénéchal, Conformal Field Theory, 1997."
    },
    {
      "name": "Delta_epsilon",
      "value": 1.0,
      "unit": "dimensionless",
      "derivation": "The scaling dimension of the energy operator epsilon is Delta = 1/2 (holo) + 1/2 (anti-holo) = 1.",
      "source": "P. Di Francesco, P. Mathieu, and D. Sénéchal, Conformal Field Theory, 1997."
    },
    {
      "name": "Delta_sigma",
      "value": 0.125,
      "unit": "dimensionless",
      "derivation": "The scaling dimension of the spin operator sigma is Delta = 1/16 (holo) + 1/16 (anti-holo) = 1/8.",
      "source": "P. Di Francesco, P. Mathieu, and D. Sénéchal, Conformal Field Theory, 1997."
    },
    {
      "name": "C_sigma_sigma_epsilon",
      "value": 0.5,
      "unit": "dimensionless",
      "derivation": "The structure constant (OPE coefficient) for the fusion sigma x sigma -> epsilon is 1/2 in the standard normalization of the Ising model.",
      "source": "P. Di Francesco, P. Mathieu, and D. Sénéchal, Conformal Field Theory, 1997."
    },
    {
      "name": "x1",
      "value": "complex (1 + i) or real (1)",
      "unit": "length (L)",
      "derivation": "The position of the first energy operator epsilon(x1). The complex coordinate represents a point in the 2D plane.",
      "source": "Task specification."
    },
    {
      "name": "x2",
      "value": "real (2)",
      "unit": "length (L)",
      "derivation": "The position of the second energy operator epsilon(x2).",
      "source": "Task specification."
    },
    {
      "name": "x3",
      "value": "real (3)",
      "unit": "length (L)",
      "derivation": "The position of the third energy operator epsilon(x3).",
      "source": "Task specification."
    },
    {
      "name": "x4",
      "value": "real (4)",
      "unit": "length (L)",
      "derivation": "The position of the first spin operator sigma(x4).",
      "source": "Task specification."
    },
    {
      "name": "x5",
      "value": "real (5)",
      "unit": "length (L)",
      "derivation": "The position of the second spin operator sigma(x5).",
      "source": "Task specification."
    }
  ]
}
```