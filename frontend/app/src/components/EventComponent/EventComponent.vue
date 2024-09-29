<template>
  <div class="event">
    <div class="event__img"></div>
    <div class="event__data">
      <div class="event__informations">
        <div class="event__number">#{{ event.id }}</div>
        <p class="event__status">
          Status: <span class="event__statusDate">{{ event.status }}</span>
        </p>
        <p class="event__date">{{ formattedDate() }}</p>
        <p class="event__place">{{ event.place }}</p>
        <p class="event__location">Office meeting</p>
      </div>
      <div class="event__buttons" @click="goToEventDetails">
        <div class="event__clickMe">
          <p>c</p>
          <p>li</p>
          <p>ckme</p>
        </div>
        <p class="event__arrowBtn"><img src="../../img/icons/greenArrow.png" alt="" /></p>
      </div>
    </div>
  </div>
</template>

<script src="./EventComponent.vue.ts"></script>
<style src="./EventComponent.scss" scoped></style>
