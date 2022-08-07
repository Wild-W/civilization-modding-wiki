---
tags:
- EffectType
title: EFFECT_PLAYER_DIPLOMACY_AGENDA_DISTRICT_SPREAD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_DIPLOMACY_AGENDA_DISTRICT_SPREAD
>
> * Class: `Unknown`
> * Parameters:
>	* SimpleModifierDescription `Unknown`
>	* StatementKey `Unknown`

## Samples
```SQL {title="AGENDA_HAMMURABI_DISTRICTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_HAMMURABI_DISTRICTS",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_HAMMURABI_DISTRICTS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_HAMMURABI_DISTRICTS",
		"SimpleModifierDescription",
		"LOC_TOOLTIP_SAMPLE_DIPLOMACY_HAMMURABI_DISTRICT"
	),
	(
		"AGENDA_HAMMURABI_DISTRICTS",
		"StatementKey",
		"AGENDA_HAMMURABI_DISTRICTS"
	);
	
```

