---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_GOVERNMENT_BUILDING_TIER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_GOVERNMENT_BUILDING_TIER
>
> * Class: `CITIES`
> * Arguments:
>	* GovernmentBuildingTier `Integer`

## Samples

```SQL {title="REQUIRES_CITY_HAS_TIER_1_GOV_BUILDING"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_TIER_1_GOV_BUILDING",
		"REQUIREMENT_CITY_HAS_GOVERNMENT_BUILDING_TIER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_TIER_1_GOV_BUILDING",
		"GovernmentBuildingTier",
		"Tier1"
	);
	```
