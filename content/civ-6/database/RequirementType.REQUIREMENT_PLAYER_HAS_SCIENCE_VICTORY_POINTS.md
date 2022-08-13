---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_SCIENCE_VICTORY_POINTS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_SCIENCE_VICTORY_POINTS
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="TECHNOLOGY_VICTORY_POINTS_MET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Persistent,
		ProgressWeight
	)
VALUES
	(
		"TECHNOLOGY_VICTORY_POINTS_MET",
		"REQUIREMENT_PLAYER_HAS_SCIENCE_VICTORY_POINTS",
		1,
		4
	);


```
