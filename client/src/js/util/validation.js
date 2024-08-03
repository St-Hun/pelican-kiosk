const checkValue = (target, regExp) => {
  if (!regExp.test(target.value)) {
    target.closest('section').classList.add('is-valid');
  } else {
    target.closest('section').classList.remove('is-valid');
  }
};

const allPass = (target, regExp) => {
  return regExp.test(target.value);
};

export { checkValue, allPass };
