#   Copyright 2020 The PyMC Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import pytest
from . import sampler_fixtures as sf
import theano

@pytest.mark.xfail(condition=(theano.config.floatX == "float32"), reason="Fails on float32")
class TestNUTSUniform(sf.NutsFixture, sf.UniformFixture):
    n_samples = 100
    tune = 240
    burn = 40
    chains = 3
    min_n_eff = 9000
    rtol = 0.1
    atol = 0.05

# class TestNUTSUniform(sf.NutsFixture, sf.UniformFixture):
#     n_samples = 10000
#     tune = 1000
#     burn = 1000
#     chains = 4
#     min_n_eff = 9000
#     rtol = 0.1
#     atol = 0.05


class TestMetropolisUniform(sf.MetropolisFixture, sf.UniformFixture):
    n_samples = 400
    tune = 3200
    burn = 20
    chains = 1
    min_n_eff = 10000
    rtol = 0.1
    atol = 0.05


class TestSliceUniform(sf.SliceFixture, sf.UniformFixture):
    n_samples = 200
    tune = 120
    burn = 20
    chains = 1
    min_n_eff = 5000
    rtol = 0.1
    atol = 0.05


class TestNUTSUniform2(TestNUTSUniform):
    n_samples = 1200
    tune = 290
    burn = 10
    chains = 1
    min_n_eff = 9000
    rtol = 0.1
    atol = 0.05
    step_args = {'target_accept': 0.95}


class TestNUTSUniform3(sf.NutsFixture, sf.UniformFixture):
    step_args = {'target_accept': 0.80}
    min_n_eff = 9000
    rtol = 0.1
    atol = 0.05
    burn = 330
    chains = 1
    n_samples=1300
    tune=330

class TestNUTSNormal(sf.NutsFixture, sf.NormalFixture):
    n_samples = 600
    tune = 890
    burn = 120
    chains = 1
    min_n_eff = 10000
    rtol = 0.1
    atol = 0.05


class TestNUTSBetaBinomial(sf.NutsFixture, sf.BetaBinomialFixture):
    n_samples = 2000
    ks_thin = 5
    tune = 1000
    burn = 0
    chains = 2
    min_n_eff = 400


class TestNUTSStudentT(sf.NutsFixture, sf.StudentTFixture):
    n_samples = 200
    tune = 110
    burn = 10
    chains = 1
    min_n_eff = 1000
    rtol = 0.1
    atol = 0.05


@pytest.mark.skip('Takes too long to run')
class TestNUTSNormalLong(sf.NutsFixture, sf.NormalFixture):
    n_samples = 500000
    tune = 5000
    burn = 0
    chains = 2
    min_n_eff = 300000
    rtol = 0.01
    atol = 0.001


class TestNUTSLKJCholeskyCov(sf.NutsFixture, sf.LKJCholeskyCovFixture):
    n_samples = 300
    tune = 200
    burn = 10
    chains = 1
    min_n_eff = 200
