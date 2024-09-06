<template>
  <div class="searchPanel">
    <h1 class="searchPanel__title">Search panel</h1>
    <input type="text" class="searchPanel__input" placeholder="Type name, date, place..." />
    <div class="searchPanel__status">
      <p class="searchPanel__statusType active">All</p>
      <p class="searchPanel__statusType">incoming</p>
      <p class="searchPanel__statusType">ended</p>
      <p class="searchPanel__statusType">live</p>
    </div>
    <div class="searchPanel__sort">
      <div class="searchPanel__sortBy sortBy">
        <p class="sortBy__title">Sort by:</p>
        <div class="sortBy__date active">date</div>
        <div class="sortBy__status">status</div>
      </div>
      <div class="searchPanel__ascending ascending">
        <p class="ascending__title">Ascending</p>
        <div class="ascending__arrow active">
          <img src="../../img/icons/arrowUp.png" alt="" />
        </div>
        <div class="ascending__arrow">
          <img src="../../img/icons/blueArrow.png" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./SearchPanel.vue.ts"></script>
<style src="./SearchPanel.scss" scoped></style>
