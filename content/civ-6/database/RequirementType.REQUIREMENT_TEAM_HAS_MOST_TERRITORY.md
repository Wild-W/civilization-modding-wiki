---
tags:
- RequirementType
title: REQUIREMENT_TEAM_HAS_MOST_TERRITORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_HAS_MOST_TERRITORY
>
> * Class: `TEAMS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="VICTORY_TEAM_HAS_MOST_TERRITORY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VICTORY_TEAM_HAS_MOST_TERRITORY",
		"REQUIREMENT_TEAM_HAS_MOST_TERRITORY"
	);


```
