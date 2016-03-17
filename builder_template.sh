
LOCATION={location}

pyenv uninstall -f {py_env}
pyenv virtualenv --no-wheel {py_version} {py_env}
pyenv rehash

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1


echo 'Setting pyenv local to {py_env}'
pyenv local {py_env}
pyenv activate {py_env}

echo 'Installing {requirement_list}'
pip install --no-binary :all: {requirement_list}

for pkg in {lib_list}
do
	echo Installing $pkg
    LIB_LOC=$LOCATION/lib/$pkg
    (cd $LIB_LOC && python setup.py install)
done

# pyenv deactivate