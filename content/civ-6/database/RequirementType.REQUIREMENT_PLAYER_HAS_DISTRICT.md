---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_DISTRICT
>
> * Class: `PLAYERS`
> * Arguments:
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples

```SQL {title="PLAYER_HAS_GOVERNMENT_DISTRICT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_HAS_GOVERNMENT_DISTRICT_REQUIREMENT",
		"REQUIREMENT_PLAYER_HAS_DISTRICT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_HAS_GOVERNMENT_DISTRICT_REQUIREMENT",
		"DistrictType",
		"DISTRICT_GOVERNMENT"
	);
	```
