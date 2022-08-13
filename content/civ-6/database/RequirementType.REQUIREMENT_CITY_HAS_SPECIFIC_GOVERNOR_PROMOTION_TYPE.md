---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_SPECIFIC_GOVERNOR_PROMOTION_TYPE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_SPECIFIC_GOVERNOR_PROMOTION_TYPE
>
> * Class: `CITIES`
> * Arguments:
>	* GovernorPromotionType `String`
>		* [GovernorPromotions.GovernorPromotionType]
>	* Established `Boolean`

## Samples

```SQL {title="REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_MERCHANT_RENEWABLE_ENERGY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_MERCHANT_RENEWABLE_ENERGY",
		"REQUIREMENT_CITY_HAS_SPECIFIC_GOVERNOR_PROMOTION_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_MERCHANT_RENEWABLE_ENERGY",
		"Established",
		1
	),
	(
		"REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_MERCHANT_RENEWABLE_ENERGY",
		"GovernorPromotionType",
		"GOVERNOR_PROMOTION_MERCHANT_RENEWABLE_ENERGY"
	);
	```

```SQL {title="REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_AQUACULTURE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_AQUACULTURE",
		"REQUIREMENT_CITY_HAS_SPECIFIC_GOVERNOR_PROMOTION_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GOVERNOR_PROMOTION_AQUACULTURE",
		"GovernorPromotionType",
		"GOVERNOR_PROMOTION_AQUACULTURE"
	);
	```
