import model from '../model/model';
import menuRender from '../views/menu-render';
import initailize from '../controllers/menuModalController';
import * as validation from '../util/validation';

//Validation
const koReg = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/;
const numReg = /^[0-9]+$/;
const urlReg = /^http[s]?\:\/\//i;
//DOM
const $menuSet = document.querySelector('.btn-dev');
const $menuSetModal = document.querySelector('.dev-modal-container');
const $modalClose = document.querySelector('.modal-exit');
const $menuSave = document.querySelector('.modal-storage');
const $menuName = document.querySelector('.dev-name');
const $menuImg = document.querySelector('.dev-image-url');
const $menuPrice = document.querySelector('.dev-price');
const $menuSizeUpPrice = document.querySelector('.dev-size-price');
const $menuShotPrice = document.querySelector('.dev-shot-price');
const $addShotCheck = document.querySelector('.dev-shot');
const $modalForm = document.querySelector('.dev-modal-input form');

// Function

const setMenu = async (e) => {
  try {
    const menu = await model.getMenu(`/${model.state}`);
    const newMenu = {
      id: menu.length + 1,
      menuName: $menuName.value,
      imgUrl: $menuImg.value,
      price: +$menuPrice.value,
      active: false,
      shot: $addShotCheck.checked,
      shotPrice: +$menuShotPrice.value,
      sizeUpPrice: +$menuSizeUpPrice.value,
    };
    const newMenus = await model.setMenu(`/${model.state}`, newMenu);
    menuRender(newMenus);
    initailize();
    $menuName.value = '';
    $menuImg.value = '';
    $menuPrice.value = '';
    $menuShotPrice.value = '';
    $menuSizeUpPrice.value = '';
    $addShotCheck.checked = false;
    $menuSetModal.classList.toggle('active');
  } catch (e) {
    console.error(e);
  }
};

// Event
$menuSet.addEventListener('click', (e) => {
  $menuSetModal.classList.toggle('active');
  $menuSave.disabled = true;
});

$modalClose.addEventListener('click', (e) => {
  $menuSetModal.classList.toggle('active');
});

$menuSetModal.addEventListener('click', (e) => {
  if (e.target === e.currentTarget) {
    if (window.confirm('작성한 내용이 사라집니다. 이동하시겠습니까?')) {
      $menuSetModal.classList.toggle('active');
    }
  }
});

document.body.onbeforeunload = () => {
  if ($menuSetModal.classList.contains('active')) {
    return window.confirm('작성한 내용이 사라집니다. 이동하시겠습니까?')
      ? window.location.reload()
      : '';
  }
};

$menuSave.addEventListener('click', setMenu);

$modalForm.addEventListener('change', (e) => {
  if (e.target.type === 'checkbox') return;
  if (e.target.matches('.dev-name')) {
    validation.checkValue(e.target, koReg);
  } else if (e.target.matches('.dev-image-url')) {
    validation.checkValue(e.target, urlReg);
  } else {
    validation.checkValue(e.target, numReg);
  }

  $menuSave.disabled =
    validation.allPass($menuName, koReg) &&
    validation.allPass($menuPrice, numReg) &&
    validation.allPass($menuShotPrice, numReg) &&
    validation.allPass($menuSizeUpPrice, numReg) &&
    validation.allPass($menuImg, urlReg)
      ? false
      : true;
});
