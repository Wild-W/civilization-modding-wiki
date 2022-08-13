---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_MOUNTAIN_CITIES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_MOUNTAIN_CITIES
>
> * Class: `PLAYERS`
> * Arguments:
>	* Percentage `Integer`
>	* MinimumCities `Integer`
>	* DistanceToMountain `Integer`
>	* BelowPercentage `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_MOUNTAIN_CITIES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_MOUNTAIN_CITIES",
		"REQUIREMENT_PLAYER_MOUNTAIN_CITIES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_MOUNTAIN_CITIES",
		"BelowPercentage",
		0
	),
	(
		"REQUIRES_HAS_HIGH_MOUNTAIN_CITIES",
		"DistanceToMountain",
		2
	),
	(
		"REQUIRES_HAS_HIGH_MOUNTAIN_CITIES",
		"MinimumCities",
		3
	),
	(
		"REQUIRES_HAS_HIGH_MOUNTAIN_CITIES",
		"Percentage",
		65
	);
	```
