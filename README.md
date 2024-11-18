# Metric on Integers

This project explores a metric on integers, focusing on distance calculations within finitely generated sets. The metric is defined using sets where the greatest common divisor (gcd) is equal to 1. By leveraging such sets, it becomes possible to express integers as combinations of elements from the set, allowing us to compute distances to a target number.

## Background

Given a finitely generated set of integers, such as `{2, 7}`, where the gcd of the set is 1, we can compute the distance of any integer from zero using elements of the set. The distance is defined as the minimum number of operations (additions or subtractions) required to reach the target integer.

### Examples

- For the set `{2, 7}`, the distance to `11` can be computed as:
    ```
    11 = 7 + 2 + 2
    ```
    Thus, the distance is `3`.

- Similarly, the distance to `5` can be calculated as:
    ```
    5 = 7 - 2
    ```
    Thus, the distance is `2`.

This metric is useful for exploring the structure of integers in terms of combinations of finitely generated sets and has potential applications in number theory, coding theory, and discrete mathematics.

## Algorithm Description

We have developed an algorithm to compute word-lengths (word metrics between an element and the zero element) on finitely generated groups of integers.

### Inputs and Outputs

- **Inputs**:
  - `X`: List of integer generators (e.g., `X = {x₁, x₂, ..., xₙ}`)
  - `n`: The integer to compute the word-length for
- **Output**:
  - `k`: The word-length of `n` with respect to `X`

**Notation**: 
|n|<sub>X</sub> = k

We only consider finitely generating sets that generate the entire set of integers (`ℤ`).

### Algorithm Steps

#### Step 1: Ensure `<X> = ℤ`

First, we must ensure that `X` generates all of `ℤ`.

**Theorem**:

Suppose `X ⊆ ℤ`.

- `gcd(X) = 1` if and only if `X` generates `ℤ`.

This is proven using Bézout's Lemma.

- By the theorem, we only require that `gcd(X) = 1`, which we can easily check using Euclid's Lemma.

#### Step 2: Compute Word-Length Using a Lemma

We now require a fast way to compute the word-length of `n` with respect to `X`. We utilize the following lemma:

**Lemma**:

Suppose `X` is a finitely generated subset of `ℤ` that generates `ℤ`, with `|X| = k`. We define:

**Definition of M**:

<div align="center">
  M = ( (x<sub>1</sub> + x<sub>2</sub>) / 2 ) * x<sub>1</sub> + ( (x<sub>2</sub> + x<sub>3</sub>) / 2 ) * x<sub>2</sub> + ... + ( (x<sub>k-1</sub> + x<sub>k</sub>) / 2 ) * x<sub>k-1</sub> + x<sub>k</sub>
</div>

where \(x<sub>i</sub>\) is the \(i\)-th term when we order `X`.

### Recurrence Relation

For all \( n > M \):
<div align="center">
  |n|<sub>X</sub> = |n - x<sub>k</sub>|<sub>X</sub> + 1
</div>

**Strategy**: Precompute all \( |n|<sub>X</sub> \) for \( n ≤ M \), then use the recurrence to compute \( |n|<sub>X</sub> \) for larger \( n \).

#### Step 3: Pseudocode

Given the ordered generating set \( X = \{x₁, x₂, ..., xₖ\} ⊆ ℤ \), the word length \( |n|<sub>X</sub> \) of any integer \( n ∈ ℤ \) can be computed as follows:

- **Input**: \( X = \{x₁, x₂, ..., xₖ\} \) (ordered set), \( n \) (target integer) 
- **Output**: \( |n|<sub>X</sub> \) (word-length of \( n \) with respect to \( X \))

### Example Calculations

- **Example 1**: For the set `X = {2, 7}`:

  - **Compute `M`**:
    ```
    x₁ = 2, x₂ = 7
    M = ((2 + 7)/2) * 2 + 7 = (9/2) * 2 + 7 = 9 + 7 = 16
    ```
  
  - **Precompute word-lengths for n ≤ 16**.

  - **Compute \( |11|<sub>X</sub> \)**:
    - Since `11 ≤ 16`, we find:
      ```
      11 = 2 + 7 + 2
      ```
      So, \( |11|<sub>X</sub> = 3 \).

  - **Compute \( |5|<sub>X</sub> \)**:
    - Since `5 ≤ 16`, we find:
      ```
      5 = 7 - 2
      ```
      So, \( |5|<sub>X</sub> = 2 \).

- **Example 2**: For \( n > M \), say `n = 20`:
  - Since `20 > 16`, apply the recurrence relation:
    \[
    |20|<sub>X</sub> = |20 - 7|<sub>X</sub> + 1 = |13|<sub>X</sub> + 1
    \]
  
  - Assuming we've precomputed \( |13|<sub>X</sub> = 3 \), then:
    \[
    |20|<sub>X</sub> = 3 + 1 = 4
    \]

## Applications

This algorithm is useful for exploring combinatorial properties of integers and has applications in number theory, discrete mathematics, and optimization problems involving linear combinations of integers.

## References

- **Bézout's Lemma**: Fundamental in number theory, stating that if `a` and `b` are integers with gcd `d`, then there exist integers `x` and `y` such that `a*x + b*y = d`.
- **Euclid's Lemma**: If a prime `p` divides the product of two integers `a*b`, then `p` divides `a` or `p` divides `b`.

# Metric on 4x4 Heisenburg Groups (H(4))

## Background



