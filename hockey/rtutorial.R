







draft_data <- read_xlsx("2018_nhl_draft_data.rds")
draft_data %>%
  ggplot(aes(x = height, y = weight)) +
  geom_point() +
  labs(x = "Height",
       y = "Weight",
       title = "Height and Weight for 2018 Drafted Players",
       subtitle = "Data from EliteProspects",
       caption = "Evan Oppenheimer") +
  theme_bw() + 
  geom_smooth()
