// Histogram.cc
//
// Produce the histograms of theoretical R* values for quantum and uniform, as
// well as the experimental histogram
//
// Input files:
//   * data/experimental/timetagged.dat
//   * data/experimental/unitary.dat
//
// Output files:
//   * histogram.dat (theoretical curves)
//   * RstarData.dat (experimental data)

#include <fstream>
#include <vector>

#include <bosonsamp/matrix.h>
#include <bosonsamp/combinatorics.h>
#include <bosonsamp/sampling.h>

#include <verification/discriminators.h>
#include <verification/input.h>
#include <verification/probabilities.h>

int main(int argc, char** argv){
  uint nmodes=9,nphotons=3,nbins=120,seed=314;
  uint nunitaries=100000,nevents=20,ntotal=nunitaries*nevents;
  double rstarq,rstaru,xrange=3.8,binwidth=xrange*1./(double)nbins,
    incr=1./(double)ntotal/binwidth;
  double *hist_q=new double[nbins], *hist_u=new double[nbins];
  gsl_rng* rng=gsl_rng_alloc(gsl_rng_mt19937);
  matrix<std::complex<double> > u;
  combination cu(nmodes,nphotons),cq(nmodes,nphotons);
  sampler_uniform uniform(nmodes);
  sampler_exact quantum;
  std::ofstream fout("../data/histogram.dat");
  std::vector<std::vector<combination> > expdata=
    getData("../data/timetagged.dat");
  if (argc>1){
    seed=atoi(argv[1]);
  }
  gsl_rng_set(rng, seed);

  for (uint i=0; i<nunitaries; i++){
    u = haar(nmodes,gsl_rng_get(rng));
    quantum = sampler_exact(u,nphotons);
    for (uint j=0; j<nevents; j++){
      cq = quantum.get();
      cu = uniform.get(nphotons);
      rstarq = R_star(u,cq);
      rstaru = R_star(u,cu);
      if (rstarq < xrange){
        hist_q[(int)(rstarq*(double)nbins/xrange)]+=incr;
      }
      if (rstaru < xrange){
        hist_u[(int)(rstaru*(double)nbins/xrange)]+=incr;
      }
    }
  }

  fout << "R* quantum uniform" << std::endl;
  for (uint i=0; i<nbins; i++){
    fout << (0.5+(double)i)*binwidth << " " << hist_q[i] << " " << hist_u[i] <<
      std::endl;
  }

  fout.close();

  nevents=expdata.size()/2;
  ntotal=0;
  nbins=18;
  binwidth=xrange*1./(double)nbins;
  u = fromFile("../data/unitary.dat",9);
  delete[] hist_q;
  hist_q = new double[nbins];
  for (uint i=0; i<nbins; i++){
    hist_q[i]=0;
  }
  for (uint i=0; i<nevents; i++){
    ntotal += expdata[i].size();
  }
  incr=1./(double)ntotal/binwidth;

  fout.open("../data/RstarData.dat");
  for (uint i=0; i<nevents; i++){
    for (uint j=0; j<expdata[i].size(); j++){
      cq = expdata[i][j];
      rstarq = R_star(u,cq);
      if (rstarq<xrange){
        hist_q[(int)(rstarq*(double)nbins/xrange)]+=incr;
      }
    }
  }

  fout << "# R* experiment" << std::endl;
  for (uint i=0; i<nbins; i++){
    fout << (0.5+(double)i)*binwidth << " " << hist_q[i] << std::endl;
  }

  fout.close();

  gsl_rng_free(rng);
  delete[] hist_q;
  delete[] hist_u;
  
  return 0;
}
