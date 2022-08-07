---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_ETHIOPIAN_HIGHLANDS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_ETHIOPIAN_HIGHLANDS
>
> * Class: `Unknown`
> * Parameters:
>	* StatementKey `Unknown`

## Samples
```SQL {title="AGENDA_MODIFIER_CITIES_NEAR_HILLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_MODIFIER_CITIES_NEAR_HILLS",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_ETHIOPIAN_HIGHLANDS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_MODIFIER_CITIES_NEAR_HILLS",
		"StatementKey",
		"LOC_PLACEHOLDER"
	);
	
```

