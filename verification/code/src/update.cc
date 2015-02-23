// update.cc
//
// Perform the Bayesian updating on 3-photon random unitary data
//
// Files required :
//   * ../data/3photon_timetagged.dat
//   * ../data/unitary.dat
//
// Output file:
//   * ../data/updating.dat

#include "heads/update.h"

#include <iostream>
#include <fstream>
#include <vector>

#include <bosonsamp/matrix.h>
#include <bosonsamp/combinatorics.h>
#include <bosonsamp/sampling.h>

#include <verification/bayes.h>
#include <verification/probabilities.h>
#include <verification/input.h>

int main(int argc, char** argv){
  uint nbins=699, nmodes=9, nphotons=3, nclicks=0;
  std::vector<std::vector<combination> > timetagged=
    getData("../data/3photon_timetagged.dat");
  matrix<std::complex<double> > u=fromFile("../data/unitary.dat",
    nmodes);
  u.print();
  std::ofstream fout("../data/updating.dat");
  estimator p_uniform(u, nphotons, pdf::RStarUniform, normalise::trivial),
    p_quantum(u, nphotons, pdf::RStarQuantum, normalise::trivial);
  std::vector<double> prob(2, 0.5);
  std::vector<estimator> EgivenH;
  EgivenH.push_back(p_quantum);
  EgivenH.push_back(p_uniform);
  updater up(prob, EgivenH);

  fout << "T quantum uniform nclicks" << std::endl;
  fout << "0 " << prob[0] << " " << prob[1] << " " << nclicks << std::endl;
  for (uint i=0; i<nbins; i++){
    nclicks += timetagged[i].size();
    prob=up.update(timetagged[i]);
    fout << i << " " << prob[0] << " " << prob[1] << " " << nclicks <<
      std::endl;
  }

  fout.close();
  return 0;
}
