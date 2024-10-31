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
      text: 
      
      design:
        columns: '1'

  - block: slider
    content:
      slides:
      - title: 
        content: 
        align: 
        background:
          image:
            filename: 47a0a3fa0709389dac09531ed82d58b.jpg
            filters:
              brightness: 1
          position: right

      - title: 
        content: 
        align: 
        background:
          image:
            filename: 9648088d130e1e9ffd81e8ee2221fdb.jpg
            filters:
              brightness: 1
          position: center

      - title:
        content: 
        align: 
        background:
          image:
            filename: a36ff071733481491d387d05cb2a6aa.jpg
            filters:
              brightness: 1
          position: center
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: false
      # Automatically transition through slides?
      loop: ture
      # Duration of transition between slides (in ms)
      interval: 2000

---