---
layout: academic
title: "Min Wang"
permalink: /
author_profile: false
---

<div class="home-columns">
<aside class="home-profile" aria-label="Profile and contact">
{% assign portrait = site.static_files | where: 'path', '/images/min-wang.jpeg' | first %}
{% if portrait %}<img class="portrait" src="{{ '/images/min-wang.jpeg' | relative_url }}" alt="Min Wang enjoying a sunset in an open meadow" width="4032" height="2268">{% endif %}
<h1>Min Wang</h1>
<p><strong>Assistant Professor</strong><br>Department of Mathematics<br>University of Houston</p>
<p>Houston, Texas, USA</p>
<a class="contact-email" href="mailto:mwang55@cougarnet.uh.edu">mwang55@cougarnet.uh.edu</a>
<p class="scholar-link"><a href="{{ site.author.googlescholar | escape }}">Google Scholar</a></p>
</aside>
<div class="home-content">
<h2 class="home-heading">About</h2>
<p>I work at the intersection of artificial intelligence and computational mathematics, developing reliable and efficient methods for complex systems.</p>
<h2>Education</h2>
<ul class="plain-list">
<li><strong>Ph.D. in Mathematics</strong><br>Texas A&amp;M University, 2019<br>Advisors: Yalchin Efendiev and Eric T. Chung</li>
<li><strong>B.Sc. in Mathematics</strong><br>Jilin University, 2014</li>
</ul>
<h2>Postdoctoral training</h2>
<ul class="plain-list">
<li><strong>Phillip Griffiths Assistant Research Professor</strong><br>Duke University, 2019–2022<br>Mentor: Jianfeng Lu</li>
<li><strong>Postdoctoral Research Associate</strong><br>ICERM, Brown University, January–May 2020</li>
</ul>
<section class="news" aria-labelledby="news-title">
<h2 id="news-title">News</h2>
{% assign news_items = site.data.news | sort: 'date' | reverse %}
<ol class="news-timeline">
{% for item in news_items limit:3 %}{% include news-entry.html %}{% endfor %}
</ol>
{% if news_items.size > 3 %}
<details class="news-archive">
<summary>Earlier news ({{ news_items.size | minus: 3 }})</summary>
<ol class="news-timeline">
{% for item in news_items offset:3 %}{% include news-entry.html %}{% endfor %}
</ol>
</details>
{% endif %}
</section>
</div>
</div>
