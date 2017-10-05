---
layout: post
title:  "About Manifolds in Machine Learning"
date:   2017-10-03 16:39:53 -0700
categories: posts 
comments: true
---

We frequently hear a word `manifold` uttered by researchers in conferences. 
Often it is accompanied by a picture of a curvy surface, sometimes resembling the image of an old manuscript.
I felt uncomfortable that there must be a formal definition of a manifold and I don't know it. Without understanding the fundamentals the attempts to understand the
things build on top of them is inefficient. So I spend quite some time reading a section from my math book on multivariable calculus that led to the definition of a
manifold. The formal definition is this:

*A set M with a defined on it finite or countable atlas, that satisfies the condition of separability, is called a (smooth) manifold.*

Here is a short explanation, which you can skip. Set M represents all points of an arbitraty surface, not necessarily tied to any coordinate system. 
We can define an injective image from a subset of M into a set of points in $$\mathbb{R}^n$$, called a map.
It is rarely possible to define a single map that will cover the entire set M and which is easy to work with. That's why several maps are required. The set of
maps that cover M (with certain additional restrictions) is called an atlas. The analogy is a globe, for which the atlas consists of two maps, one of the western hemisphere
and another of the eastern hemisphere. 

However, when reading a [deep learning book](#references), section `5.11.3 Manifold Learning`, I discovered that the word `manifold` in machine learning isn't used with the mathematical rigor like above.
There `manifold` is described as just a surface (a set of connected points) in a space, which dimension (degrees of freedom) is smaller than that of the space
it resides. For example, a curve in a 2D plane. Locally it has one degree of freedom (DOF) only, by moving along the tangent line at a point. 
Generally the dimensionality (number of dimensions) in one point can be different from the dimensionality in another point. As the example in the text goes,
imagine a digit 8 drawn on a plane. Everywhere except the intersection point it has one DOF, while in the intersection point is has two DOFs.

The central idea of manifold learning is that the real data, such as images or speech, lies on a low-dimensional manifold inside a high-dimensional space. The
simple experiment is this. Create a random generator of a $$NxN$$  matrix, restricting its values to integers in range $$[0, 255]$$.
Generate as many matrices as you wish, and I doubt you'll get at least one case that looks like a real image. The probability of getting a real image is
infinitely small. We can say that among all possible points in space $$\mathbb{R}^n$$, real images occupy a tiny portion.
This isn't enough yet to say that those points are on a manifold, we have to show that they are connected to each other.
Formally it means one had to show that there exist the first and higher-order derivatives in every point.
Of course we won't do this. Instead we conduct a second experiment, described in the same [deep learning book](#references), section `14.6 Learning Manufolds with
Autoencoders`, and the resulting `Figure 14.6`:

![png]({{ "/images/dlb_f14.6.png" | absolute_url }}){:height="400px"}

Each point in this figure represents a version of one image of 9 from MNIST dataset, translated down several pixels. We see that we can fit quite a simple curve
into these points and think of it as a manifold. 
To make this visualization, PCA was used to project 784D points (this is what you get when you flatten 28 * 28 MNIST image) onto a 2D plane.
To better understand how this figure was created, let's try to replicate this result ourselves. And it should help to understand better what manifolds are.

{% include_relative /ipynb_md/manifolds.md %}

If you are interested, you can [dowload the jupyter notebook]({{ "/ipynb/manifolds.ipynb" | absolute_url }}).


# Summary
Manifold is a connected region, locally low-dimensional, that resides in a high-dimensional space. 
Real data lies on a low-dimensional manifold. 
It is a goal of machine learning to capture the representation of the manifold.

# References

1. Deep Learning, Ian Goodfellow and Yoshua Bengio and Aaron Courville, MIT Press, [http://www.deeplearningbook.org](http://www.deeplearningbook.org), 2016
2. Канатников А.Н., Крищенко А.П., Четвериков В.Н. Дифференциальное исчисление функций многих переменных. Москва: Издательство МГТУ им. Н.Э. Баумана, 2000. 

<!--
```
@book{Goodfellow-et-al-2016,
    title={Deep Learning},
    author={Ian Goodfellow and Yoshua Bengio and Aaron Courville},
    publisher={MIT Press},
    note={\url{http://www.deeplearningbook.org}},
    year={2016}
}
```
-->
