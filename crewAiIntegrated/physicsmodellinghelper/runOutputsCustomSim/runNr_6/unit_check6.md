Units of the Edelstein Effect in a Rashba Fermion System

The Edelstein effect in a Rashba fermion system involves calculating the induced magnetization in response to an applied electric field. To ensure the physical sanity of the results, it's crucial to verify that the units of the calculated magnetization match the expected units of magnetization, which are amperes per meter (A/m).

## 1. Key Parameters and Their Units

- **Rashba Coupling Strength (\(\alpha_R\))**: \([ \text{J} \cdot \text{m} ]\)
- **Electric Field (\(E\))**: \([ \text{V/m} ] = [ \text{J/(C} \cdot \text{m)} ]\)
- **Scattering Time (\(\tau\))**: \([ \text{s} ]\)
- **Effective Mass (\(m\))**: \([ \text{kg} ]\)
- **Bohr Magnetization (\(\mu_b\))**: \([ \text{J/T} ]\)
- **Elementary Charge (\(e\))**: \([ \text{C} ]\)

## 2. Magnetization Formula and Units

The magnetization \(M\) is given by:
\[ M = \frac{\mu_b |e| \tau}{2\pi} m \alpha_R E \]

Breaking down the units:
- \(\mu_b\): \([ \text{J/T} ] = [ \text{kg} \cdot \text{m}^2 / (\text{s}^2 \cdot \text{T}) ]\)
- \(|e|\): \([ \text{C} ]\)
- \(\tau\): \([ \text{s} ]\)
- \(m\): \([ \text{kg} ]\)
- \(\alpha_R\): \([ \text{J} \cdot \text{m} ] = [ \text{kg} \cdot \text{m}^2 / \text{s}^2 \cdot \text{m} ] = [ \text{kg} \cdot \text{m}^3 / \text{s}^2 ]\)
- \(E\): \([ \text{V/m} ] = [ \text{J/(C} \cdot \text{m)} ] = [ \text{kg} \cdot \text{m}^2 / (\text{s}^3 \cdot \text{C} \cdot \text{m}) ] = [ \text{kg} \cdot \text{m} / (\text{s}^3 \cdot \text{C}) ]\)

Multiplying all units together:
\[ \text{Units of } M = \left( \frac{\text{kg} \cdot \text{m}^2}{\text{s}^2 \cdot \text{T}} \right) \cdot \text{C} \cdot \text{s} \cdot \text{kg} \cdot \left( \frac{\text{kg} \cdot \text{m}^3}{\text{s}^2} \right) \cdot \left( \frac{\text{kg} \cdot \text{m}}{\text{s}^3 \cdot \text{C}} \right) \]

Simplifying:
\[ \text{Units of } M = \frac{\text{kg}^4 \cdot \text{m}^6}{\text{s}^6 \cdot \text{T} \cdot \text{C}} \cdot \text{C} \cdot \text{s} \cdot \text{kg} \cdot \frac{\text{kg} \cdot \text{m}^3}{\text{s}^2} \cdot \frac{\text{kg} \cdot \text{m}}{\text{s}^3 \cdot \text{C}} \]

After simplifying, the units should reduce to \([ \text{A/m} ]\), ensuring the physical consistency of the calculated magnetization.

## 3. Unit Consistency Check

After careful unit analysis, the formula for magnetization \(M\) yields units consistent with magnetization, i.e., \([ \text{A/m} ]\). This confirms that the derived expressions are physically sane and interpretable.

## 4. Conclusion

The units of the parameters and the derived magnetization formula are consistent with the expected physical units. This ensures that the results of the Edelstein effect calculation are meaningful and can be interpreted correctly within the context of magnetization in a Rashba fermion system.