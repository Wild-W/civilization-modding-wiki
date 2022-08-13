---
tags:
- RequirementType
title: REQUIREMENT_CITY_TRANSFER_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_TRANSFER_TYPE_MATCHES
>
> * Class: `CITIES`
> * Arguments:
>	* TransferType `String`
>		* BY_COMBAT>		  BY_COMBAT_ORIGINAL_OWNER>		  BY_COMBAT_OWNER_BEFORE_OCCUPATION>		  BY_CULTURAL_IDENTITY>		  BY_GIFT>		  BY_LIBERATION>		  BY_SETTLER

## Samples

```SQL {title="CITY_FOUNDED_BY_SETTLER_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CITY_FOUNDED_BY_SETTLER_REQUIREMENT",
		"REQUIREMENT_CITY_TRANSFER_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"CITY_FOUNDED_BY_SETTLER_REQUIREMENT",
		"TransferType",
		"BY_SETTLER"
	);
	
```
