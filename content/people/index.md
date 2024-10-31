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
      text: |
        <figure class="half">
           <img src="47a0a3fa0709389dac09531ed82d58b.jpg" alt="图片描述"width="200" height="auto">
           <img src="a36ff071733481491d387d05cb2a6aa.jpg" alt="图片描述"width="200" height="auto">
           <img src="9648088d130e1e9ffd81e8ee2221fdb.jpg" alt="图片描述"width="200" height="auto">
        </figure>
      design:
        columns: '2'


---