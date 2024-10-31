---
title: People
date: 2024-10-24

type: landing

sections:
  - block: people
    content:
      title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Principal Investigators
          - Postdocs
          - PhD Students
          - Masters Students
          - Undergraduate Students
          - Administration
          - Visitors
          - Alumni
          
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true

  - block: markdown
    content:
      title: Photo Gallery
      subtitle: Snapshots of Togetherness — Our Team Story

  - block: cta-image-paragraph
    content:
      items:
        - title: 20xx团建聚餐
          text: xxxxx
          feature_icon: check
          features:
            - "xxxxx"
            - "xxxxxx"
            - "xxxxxxx"
          # Upload image to `assets/media/` and reference the filename here
          image: 47a0a3fa0709389dac09531ed82d58b.jpg

        - title: 20xx毕业留念
          text: xxxxx
          feature_icon: check
          features:
            - "xxxxx"
            - "xxxxxx"
            - "xxxxxxx"
          # Upload image to `assets/media/` and reference the filename here
          image: a36ff071733481491d387d05cb2a6aa.jpg

        - title: 20xx竞赛留念
          text: 中国研究生创新机器人设计大赛
          feature_icon: bolt
          features:
            - "xxx"
            - "xxxxx"
            - "xxxxxxxxxx"
          # Upload image to `assets/media/` and reference the filename here
          image: 9648088d130e1e9ffd81e8ee2221fdb.jpg
          button:
            text: Join
            url: https://cpipc.acge.org.cn/cw/hp/2c9088a5696cbf370169a3f8934810be
    design:
      # Section background color (CSS class)
      css_class: "bg-gray-100 dark:bg-gray-900"


  - block: slider
    content:
      title: Photo Gallery
      subtitle: Snapshots of Togetherness — Our Team Story
      slides:
      - title: 
        content: 
        align: center
        background:
          image:
            filename: 47a0a3fa0709389dac09531ed82d58b.jpg
            filters:
              brightness: 1
          position: center

      - title: 
        content: 
        align: center
        background:
          image:
            filename: 9648088d130e1e9ffd81e8ee2221fdb.jpg
            filters:
              brightness: 1
          position: center

      - title: 
        content: 
        align: center
        background:
          image:
            filename: a36ff071733481491d387d05cb2a6aa.jpg
            filters:
              brightness: 1
          position: center
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '900'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000
      view: card


---

