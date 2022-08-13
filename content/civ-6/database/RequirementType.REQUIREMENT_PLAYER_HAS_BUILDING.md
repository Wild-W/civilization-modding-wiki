---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_BUILDING
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_BUILDING
>
> * Class: `PLAYERS`
> * Arguments:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="PLAYER_HAS_GOV_BUILDING_CITYSTATES_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_HAS_GOV_BUILDING_CITYSTATES_REQUIREMENT",
		"REQUIREMENT_PLAYER_HAS_BUILDING"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_HAS_GOV_BUILDING_CITYSTATES_REQUIREMENT",
		"BuildingType",
		"BUILDING_GOV_CITYSTATES"
	);
	
```
