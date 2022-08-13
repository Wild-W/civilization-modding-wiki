---
tags:
- RequirementType
title: REQUIREMENT_UNIT_PROMOTION_CLASS_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_PROMOTION_CLASS_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* UnitPromotionClass `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples

```SQL {title="RECON_UNITS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"RECON_UNITS",
		"REQUIREMENT_UNIT_PROMOTION_CLASS_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"RECON_UNITS",
		"UnitPromotionClass",
		"PROMOTION_CLASS_RECON"
	);
	```
