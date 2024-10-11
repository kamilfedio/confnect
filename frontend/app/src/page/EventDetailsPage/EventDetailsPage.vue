<template>
  <div class="event">
    <div class="event__details details">
      <div class="details__name">{{ event.name }}</div>
      <div class="details__statDate">
        <div class="details__status">{{ event.status }}</div>
        <div class="details__date">{{ event.date }}</div>
      </div>
      <div class="details__description">{{ event.description }}</div>
      <button class="event__editBtn">Edit</button>
      <button class="event__startBtn">Start event</button>
    </div>
    <div class="event__questions">questions</div>
    <div class="event__feedback">feedback</div>
  </div>
</template>

<script src="./EventDetailsPage.vue.ts"></script>
<style src="./EventDetailsPage.scss" scoped></style>
