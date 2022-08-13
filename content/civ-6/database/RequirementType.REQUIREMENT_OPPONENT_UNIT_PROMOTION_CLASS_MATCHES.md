---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_UNIT_PROMOTION_CLASS_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_UNIT_PROMOTION_CLASS_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* UnitPromotionClass `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples

```SQL {title="OPPONENT_IS_NOT_CAVALRY_UNIT_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_IS_NOT_CAVALRY_UNIT_REQUIREMENTS",
		"REQUIREMENT_OPPONENT_UNIT_PROMOTION_CLASS_MATCHES"
	);

```

```SQL {title="ANTI_CAVALRY_OPPONENT_PROMOTION_CLASS_REQUIREMENT_HC"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"ANTI_CAVALRY_OPPONENT_PROMOTION_CLASS_REQUIREMENT_HC",
		"REQUIREMENT_OPPONENT_UNIT_PROMOTION_CLASS_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"ANTI_CAVALRY_OPPONENT_PROMOTION_CLASS_REQUIREMENT_HC",
		"UnitPromotionClass",
		"PROMOTION_CLASS_HEAVY_CAVALRY"
	);
	```
