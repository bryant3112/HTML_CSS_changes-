
I fixed the layout issues by adding spacing between clubs and connecting the HTML with CSS so the design applies correctly.


<div class="club-box">
  <article class="card">
    <time class="date">
      {{ club.published_date }}
    </time>

    <h2>
      <a href="{% url 'club_detail' club.pk %}">
        {{ club.title }}
        </a>
    </h2>

    <p><strong>Interested:</strong> {{ club.interest }}</p>
    <p><strong>Days:</strong> {{ club.days }}</p>
    <p><strong>Time:</strong> {{ club.start_time }} - {{ club.end_time }}</p>
    <p><strong>Location:</strong> {{ club.location }}</p>
   </article>
</div>

HTML Changes 



CSS Changes

.club-box {
  border: 2px solid #800086;
  padding: 15px;
  margin-bottom: 20px;
  border-radius: 8px;
  background-color: white;
}

.card {
  margin-top: 10px;
}