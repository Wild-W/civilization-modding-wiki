---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_CITY_ON_EMERGENCY_PLOT_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_CITY_ON_EMERGENCY_PLOT_CONTINENT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_EMERGENCY_TARGET_IS_ON_CONTINENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_EMERGENCY_TARGET_IS_ON_CONTINENT",
		"REQUIREMENT_PLAYER_HAS_CITY_ON_EMERGENCY_PLOT_CONTINENT"
	);


```
