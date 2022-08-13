---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_DISTRICT
>
> * Class: `CITIES`
> * Arguments:
>	* MustBeFunctioning `Boolean`
>		* Require the district to be functioning (not pillaged).
>		* [Buildings.BuildingType]
>	* DistrictType `String`
>		* The type of the district to check for.
>		* [Districts.DistrictType]

## Samples

```SQL {title="FOREIGN_CITY_REQUIRES_CITY_HAS_ROYAL_NAVY_DOCKYARD"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"FOREIGN_CITY_REQUIRES_CITY_HAS_ROYAL_NAVY_DOCKYARD",
		"REQUIREMENT_CITY_HAS_DISTRICT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"FOREIGN_CITY_REQUIRES_CITY_HAS_ROYAL_NAVY_DOCKYARD",
		"DistrictType",
		"DISTRICT_ROYAL_NAVY_DOCKYARD"
	),
	(
		"FOREIGN_CITY_REQUIRES_CITY_HAS_ROYAL_NAVY_DOCKYARD",
		"MustBeFunctioning",
		0
	);
	```
