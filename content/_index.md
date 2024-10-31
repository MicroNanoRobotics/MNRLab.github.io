---
# Leave the homepage title empty to use the site title
title:
date: 2024-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        微纳机器人研究团队
        
      image:
        filename: wanghuaping2.jpg
      text: |
        <br>
          The Lab is committed to magnetic drive software robots, micro and nano robots, micro-scale automation and other fields of research.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title: 
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: cover3.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: contain
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest article
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article-journal'
    design:
      view: citation
      columns: '5'

  - block: markdown
    content:
      title: Photo Gallery
      subtitle: Snapshots of Togetherness — Our Team Story
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
        
    design:
      columns: '1'


  - block: slider
    content:
      title: Photo Gallery
      subtitle: Snapshots of Togetherness — Our Team Story
      slides:
      - title: 
        content: ![alt text](47a0a3fa0709389dac09531ed82d58b.jpg)47a0a3fa0709389dac09531ed82d58b.jpg
        align: center

      - title: 
        content: 9648088d130e1e9ffd81e8ee2221fdb.jpg
        align: center


      - title: 
        content: a36ff071733481491d387d05cb2a6aa.jpg
        align: center

    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_width: '900'
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000
      view: card

---
